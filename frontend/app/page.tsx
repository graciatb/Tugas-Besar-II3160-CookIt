'use client'
import {
    Flex,
    Box,
    Stack,
    Button,
    Heading,
    Text,
  } from "@chakra-ui/react"
import { Link } from '@chakra-ui/next-js'
import { Image } from '@chakra-ui/react'

export default function Page() {
    return (
        <Flex
          align="center"
          justify={{ base: "center", md: "space-around", xl: "space-between" }}
          minH="100vh"
          px={8}
        >
          <Stack
            spacing={5}
            w={{ base: "80%", md: "40%" }}
            align={["center", "flex-start"]}
            ml={{xl: "15"}}
          >
            <Heading
              as="h1"
              size="xl"
              fontWeight="bold"
              color="orange.600"
              textAlign={["center", "center", "left", "left"]}
            >
              It's CookIt Time! 
            </Heading>
            <Heading
              as="h2"
              size="md"
              color="primary.800"
              opacity="0.8"
              fontWeight="normal"
              lineHeight={1.5}
              textAlign={["center", "center", "left", "left"]}
            >
              The best way to find recipes and order the ingredients,
              make your cooking easier and more fun! ⭐
            </Heading>
            <Link href="/login">
              <Button
                bg="orange.500"
                color='white'
                borderRadius="8px"
                py="4"
                px="4"
                lineHeight="1"
                size="md"
              >
                Log In to CookIt
              </Button>
            </Link>
            <Text
              fontSize="xs"
              mt={2}
              textAlign="center"
              color="primary.800"
              opacity="0.6"
            >
              Or sign up to CookIt
            </Text>
          </Stack>
          <Box w={{ base: "60%", sm: "60%", md: "50%" }}>
            <Image src="https://images.ctfassets.net/hphe2swm9scr/23xisz0emMqQYbQF8fI7Mk/5e7a28d71c1f2486a22fca6e26a65bb5/Festive_HP_v1.jpg" rounded="1rem" shadow="2xl" />
          </Box>
        </Flex>
      );
    }